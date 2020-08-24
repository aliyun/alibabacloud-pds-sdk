<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\Credentials;

use Exception;

class PDSCredentials
{
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
        throw new Exception('Un-implemented');
    }
}
