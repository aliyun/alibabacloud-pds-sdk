<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\LdapConfig;

/**
 * *
 */
class AuthConfig extends Model {
    protected $_name = [
        'appId' => 'app_id',
        'appSecret' => 'app_secret',
        'callbackSecurity' => 'callback_security',
        'enable' => 'enable',
        'endpoint' => 'endpoint',
        'enterpriseId' => 'enterprise_id',
        'ldapConfig' => 'ldap_config',
        'loginPageHeaders' => 'login_page_headers',
        'loginPageTemplate' => 'login_page_template',
        'loginPageVars' => 'login_page_vars',
        'whiteListConfig' => 'white_list_config',
        'whiteListEnable' => 'white_list_enable',
    ];
    public function validate() {}
    public function toMap() {
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
        if (null !== $this->ldapConfig) {
            $res['ldap_config'] = null !== $this->ldapConfig ? $this->ldapConfig->toMap() : null;
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
        if (null !== $this->whiteListConfig) {
            $res['white_list_config'] = $this->whiteListConfig;
        }
        if (null !== $this->whiteListEnable) {
            $res['white_list_enable'] = $this->whiteListEnable;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return AuthConfig
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['app_secret'])){
            $model->appSecret = $map['app_secret'];
        }
        if(isset($map['callback_security'])){
            $model->callbackSecurity = $map['callback_security'];
        }
        if(isset($map['enable'])){
            $model->enable = $map['enable'];
        }
        if(isset($map['endpoint'])){
            $model->endpoint = $map['endpoint'];
        }
        if(isset($map['enterprise_id'])){
            $model->enterpriseId = $map['enterprise_id'];
        }
        if(isset($map['ldap_config'])){
            $model->ldapConfig = LdapConfig::fromMap($map['ldap_config']);
        }
        if(isset($map['login_page_headers'])){
            $model->loginPageHeaders = $map['login_page_headers'];
        }
        if(isset($map['login_page_template'])){
            $model->loginPageTemplate = $map['login_page_template'];
        }
        if(isset($map['login_page_vars'])){
            $model->loginPageVars = $map['login_page_vars'];
        }
        if(isset($map['white_list_config'])){
            $model->whiteListConfig = $map['white_list_config'];
        }
        if(isset($map['white_list_enable'])){
            $model->whiteListEnable = $map['white_list_enable'];
        }
        return $model;
    }
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
     * @var LdapConfig
     */
    public $ldapConfig;

    /**
     * @var mixed[]
     */
    public $loginPageHeaders;

    /**
     * @var string
     */
    public $loginPageTemplate;

    /**
     * @var mixed[]
     */
    public $loginPageVars;

    /**
     * @var mixed[]
     */
    public $whiteListConfig;

    /**
     * @var bool
     */
    public $whiteListEnable;

}
