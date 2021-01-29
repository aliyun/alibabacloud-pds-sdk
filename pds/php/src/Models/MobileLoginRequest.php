<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class MobileLoginRequest extends Model {
    protected $_name = [
        'appId' => 'app_id',
        'autoRegister' => 'auto_register',
        'captchaId' => 'captcha_id',
        'captchaText' => 'captcha_text',
        'encryptedKey' => 'encrypted_key',
        'nvcParam' => 'nvc_param',
        'password' => 'password',
        'phoneNumber' => 'phone_number',
        'phoneRegion' => 'phone_region',
        'smsCode' => 'sms_code',
        'smsCodeId' => 'sms_code_id',
    ];
    protected $_default = [
        'autoRegister' => 'false',
    ];
    public function validate() {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('nvcParam', $this->nvcParam, true);
        Model::validateRequired('phoneNumber', $this->phoneNumber, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->autoRegister) {
            $res['auto_register'] = $this->autoRegister;
        }
        if (null !== $this->captchaId) {
            $res['captcha_id'] = $this->captchaId;
        }
        if (null !== $this->captchaText) {
            $res['captcha_text'] = $this->captchaText;
        }
        if (null !== $this->encryptedKey) {
            $res['encrypted_key'] = $this->encryptedKey;
        }
        if (null !== $this->nvcParam) {
            $res['nvc_param'] = $this->nvcParam;
        }
        if (null !== $this->password) {
            $res['password'] = $this->password;
        }
        if (null !== $this->phoneNumber) {
            $res['phone_number'] = $this->phoneNumber;
        }
        if (null !== $this->phoneRegion) {
            $res['phone_region'] = $this->phoneRegion;
        }
        if (null !== $this->smsCode) {
            $res['sms_code'] = $this->smsCode;
        }
        if (null !== $this->smsCodeId) {
            $res['sms_code_id'] = $this->smsCodeId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return MobileLoginRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['auto_register'])){
            $model->autoRegister = $map['auto_register'];
        }
        if(isset($map['captcha_id'])){
            $model->captchaId = $map['captcha_id'];
        }
        if(isset($map['captcha_text'])){
            $model->captchaText = $map['captcha_text'];
        }
        if(isset($map['encrypted_key'])){
            $model->encryptedKey = $map['encrypted_key'];
        }
        if(isset($map['nvc_param'])){
            $model->nvcParam = $map['nvc_param'];
        }
        if(isset($map['password'])){
            $model->password = $map['password'];
        }
        if(isset($map['phone_number'])){
            $model->phoneNumber = $map['phone_number'];
        }
        if(isset($map['phone_region'])){
            $model->phoneRegion = $map['phone_region'];
        }
        if(isset($map['sms_code'])){
            $model->smsCode = $map['sms_code'];
        }
        if(isset($map['sms_code_id'])){
            $model->smsCodeId = $map['sms_code_id'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description App ID, 当前访问的App
     * @example csaklidwasdhjwid
     * @var string
     */
    public $appId;

    /**
     * @description 是否自动注册用户，使用密码登录此参数不生效
     * @example false
     * @var bool
     */
    public $autoRegister;

    /**
     * @description 图片验证码ID, 密码登录需要此参数
     * @example abc
     * @var string
     */
    public $captchaId;

    /**
     * @description 用户输入的验证码值, 密码登录需要此参数
     * @example abc
     * @var string
     */
    public $captchaText;

    /**
     * @description AES-256对称加密密钥，通过App公钥加密后传输
     * @example 123456,Abc
     * @var string
     */
    public $encryptedKey;

    /**
     * @description 环境参数
     * @example {"a":"CF_APP_1"}
     * @var string
     */
    public $nvcParam;

    /**
     * @description 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
     * @example 123456
     * @var string
     */
    public $password;

    /**
     * @description 待查询的手机号
     * @example 152*****341
     * @var string
     */
    public $phoneNumber;

    /**
     * @description 国家编号，默认86，不需要填+号，直接填数字
     * @example 86
     * @var string
     */
    public $phoneRegion;

    /**
     * @description 短信验证码内容，使用密码登录此参数不生效
     * @example 1234
     * @var string
     */
    public $smsCode;

    /**
     * @description 短信验证码ID，使用密码登录此参数不生效
     * @example csjanwia
     * @var string
     */
    public $smsCodeId;

}
