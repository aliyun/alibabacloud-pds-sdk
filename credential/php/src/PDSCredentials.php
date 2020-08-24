<?php

namespace Aliyun\PDS\Credentials;

use Adbar\Dot;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Request;
use AlibabaCloud\Tea\Tea;

class PDSCredentials
{
    public $httpConfig = [];

    protected $_endpoint;

    protected $_domainId;

    protected $_clientId;

    protected $_refreshToken;

    protected $_clientSecret;

    protected $_accessToken;

    protected $_expireTime;

    public function __construct($config)
    {
        $this->_endpoint     = $config->endpoint;
        $this->_domainId     = $config->domainId;
        $this->_clientId     = $config->clientId;
        $this->_refreshToken = $config->refreshToken;
        $this->_clientSecret = $config->clientSecret;
        $this->_accessToken  = $config->accessToken;
        $this->_expireTime   = $config->expireTime;
    }

    /**
     * @param string $expireTime
     */
    public function setExpireTime($expireTime)
    {
        $this->_expireTime = $expireTime;
    }

    /**
     * @return string
     */
    public function getExpireTime()
    {
        return $this->_expireTime;
    }

    /**
     * @return string
     */
    public function getRefreshToken()
    {
        return $this->_refreshToken;
    }

    /**
     * @param string $refreshToken
     */
    public function setRefreshToken($refreshToken)
    {
        $this->_refreshToken = $refreshToken;
    }

    /**
     * @param string $accessToken
     */
    public function setAccessToken($accessToken)
    {
        $this->_accessToken = $accessToken;
    }

    /**
     * @return string
     */
    public function getAccessToken()
    {
        if (null === $this->_accessToken) {
            throw new \RuntimeException('AccessToken is null');
        }
        if ($this->shouldRefresh(time())) {
            $this->refreshAccessToken();
        }

        return $this->_accessToken;
    }

    public function shouldRefresh($now)
    {
        if (empty($this->_expireTime) || empty($this->_refreshToken)) {
            return false;
        }

        return strtotime($this->_expireTime) - $now <= 500;
    }

    private function refreshAccessToken()
    {
        $request           = new Request();
        $request->protocol = 'http';
        $request->method   = 'POST';
        $request->pathname = '/v2/oauth/token';
        $request->headers  = [
            'host'                    => $this->getHost($this->_endpoint, $this->_domainId . '.api.aliyunpds.com'),
            'content-type'            => 'application/x-www-form-urlencoded; charset=utf-8',
            'date'                    => gmdate('Y-m-d\\TH:i:s\\Z'),
            'accept'                  => 'application/json',
            'x-acs-signature-method'  => 'HMAC-SHA1',
            'x-acs-signature-version' => '1.0',
        ];
        $bodyString        = 'grant_type=refresh_token&refresh_token=' . $this->_refreshToken
            . '&client_id=' . $this->_clientId
            . '&client_secret=' . $this->_clientSecret;
        $request->body     = $bodyString;
        $response          = Tea::send($request, $this->httpConfig);
        if ($response->getBody()->isSeekable()) {
            $response->getBody()->rewind();
        }
        $contents = $response->getBody()->getContents();
        if (200 === $response->getStatusCode()) {
            $result              = new Dot(json_decode($contents, true));
            $this->_expireTime   = $result->get('expire_time');
            $this->_accessToken  = $result->get('access_token');
            $this->_refreshToken = $result->get('refresh_token');
        } else {
            throw new TeaError(json_decode($contents));
        }
    }

    private function getHost($endpoint, $domain)
    {
        if (null !== $endpoint && \strlen(trim($endpoint)) > 0) {
            return $endpoint;
        }

        return $domain;
    }
}
