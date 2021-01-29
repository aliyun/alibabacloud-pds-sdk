<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class MobileSendSmsCodeRequest extends Model {
    protected $_name = [
        'appId' => 'app_id',
        'captchaId' => 'captcha_id',
        'captchaText' => 'captcha_text',
        'nvcParam' => 'nvc_param',
        'phoneNumber' => 'phone_number',
        'phoneRegion' => 'phone_region',
        'type' => 'type',
    ];
    public function validate() {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('nvcParam', $this->nvcParam, true);
        Model::validateRequired('phoneNumber', $this->phoneNumber, true);
        Model::validateRequired('type', $this->type, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->captchaId) {
            $res['captcha_id'] = $this->captchaId;
        }
        if (null !== $this->captchaText) {
            $res['captcha_text'] = $this->captchaText;
        }
        if (null !== $this->nvcParam) {
            $res['nvc_param'] = $this->nvcParam;
        }
        if (null !== $this->phoneNumber) {
            $res['phone_number'] = $this->phoneNumber;
        }
        if (null !== $this->phoneRegion) {
            $res['phone_region'] = $this->phoneRegion;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return MobileSendSmsCodeRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['captcha_id'])){
            $model->captchaId = $map['captcha_id'];
        }
        if(isset($map['captcha_text'])){
            $model->captchaText = $map['captcha_text'];
        }
        if(isset($map['nvc_param'])){
            $model->nvcParam = $map['nvc_param'];
        }
        if(isset($map['phone_number'])){
            $model->phoneNumber = $map['phone_number'];
        }
        if(isset($map['phone_region'])){
            $model->phoneRegion = $map['phone_region'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
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
     * @description 图片验证码ID
     * @example abc
     * @var string
     */
    public $captchaId;

    /**
     * @description 用户输入的验证码值
     * @example abc
     * @var string
     */
    public $captchaText;

    /**
     * @description 环境参数
     * @example {"a":"CF_APP_1"}
     * @var string
     */
    public $nvcParam;

    /**
     * @description 待发送验证短信的手机号
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
     * @description 验证码用途, 可下发: login、register、change_password
     * @example login
     * @var string
     */
    public $type;

}
