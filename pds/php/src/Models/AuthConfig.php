<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class AuthConfig extends Model
{
    /**
     * @var string
     */
    public $appId;

    /**
     * @var string
     */
    public $appSecret;

    /**
     * @var bool
     */
    public $callbackSecurity;

    /**
     * @var bool
     */
    public $enable;

    /**
     * @var string
     */
    public $endpoint;

    /**
     * @var string
     */
    public $enterpriseId;

    /**
     * @var array
     */
    public $loginPageHeaders;

    /**
     * @var string
     */
    public $loginPageTemplate;

    /**
     * @var array
     */
    public $loginPageVars;
    protected $_name = [
        'appId'             => 'app_id',
        'appSecret'         => 'app_secret',
        'callbackSecurity'  => 'callback_security',
        'enable'            => 'enable',
        'endpoint'          => 'endpoint',
        'enterpriseId'      => 'enterprise_id',
        'loginPageHeaders'  => 'login_page_headers',
        'loginPageTemplate' => 'login_page_template',
        'loginPageVars'     => 'login_page_vars',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->appSecret) {
            $res['app_secret'] = $this->appSecret;
        }
        if (null !== $this->callbackSecurity) {
            $res['callback_security'] = $this->callbackSecurity;
        }
        if (null !== $this->enable) {
            $res['enable'] = $this->enable;
        }
        if (null !== $this->endpoint) {
            $res['endpoint'] = $this->endpoint;
        }
        if (null !== $this->enterpriseId) {
            $res['enterprise_id'] = $this->enterpriseId;
        }
        if (null !== $this->loginPageHeaders) {
            $res['login_page_headers'] = $this->loginPageHeaders;
        }
        if (null !== $this->loginPageTemplate) {
            $res['login_page_template'] = $this->loginPageTemplate;
        }
        if (null !== $this->loginPageVars) {
            $res['login_page_vars'] = $this->loginPageVars;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return AuthConfig
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['app_id'])) {
            $model->appId = $map['app_id'];
        }
        if (isset($map['app_secret'])) {
            $model->appSecret = $map['app_secret'];
        }
        if (isset($map['callback_security'])) {
            $model->callbackSecurity = $map['callback_security'];
        }
        if (isset($map['enable'])) {
            $model->enable = $map['enable'];
        }
        if (isset($map['endpoint'])) {
            $model->endpoint = $map['endpoint'];
        }
        if (isset($map['enterprise_id'])) {
            $model->enterpriseId = $map['enterprise_id'];
        }
        if (isset($map['login_page_headers'])) {
            $model->loginPageHeaders = $map['login_page_headers'];
        }
        if (isset($map['login_page_template'])) {
            $model->loginPageTemplate = $map['login_page_template'];
        }
        if (isset($map['login_page_vars'])) {
            $model->loginPageVars = $map['login_page_vars'];
        }

        return $model;
    }
}
