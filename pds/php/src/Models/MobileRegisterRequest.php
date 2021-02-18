<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class MobileRegisterRequest extends Model
{
    public $headers;

    /**
     * @description App ID, 当前访问的App
     *
     * @example csaklidwasdhjwid
     *
     * @var string
     */
    public $appId;

    /**
     * @description 环境参数
     *
     * @example {"a":"CF_APP_1"}
     *
     * @var string
     */
    public $nvcParam;

    /**
     * @description 待查询的手机号
     *
     * @example 152*****341
     *
     * @var string
     */
    public $phoneNumber;

    /**
     * @description 国家编号，默认86，不需要填+号，直接填数字
     *
     * @example 86
     *
     * @var string
     */
    public $phoneRegion;

    /**
     * @description 短信验证码内容
     *
     * @example 1234
     *
     * @var string
     */
    public $smsCode;

    /**
     * @description 短信验证码ID
     *
     * @example csjanwia
     *
     * @var string
     */
    public $smsCodeId;
    protected $_name = [
        'appId'       => 'app_id',
        'nvcParam'    => 'nvc_param',
        'phoneNumber' => 'phone_number',
        'phoneRegion' => 'phone_region',
        'smsCode'     => 'sms_code',
        'smsCodeId'   => 'sms_code_id',
    ];

    public function validate()
    {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('nvcParam', $this->nvcParam, true);
        Model::validateRequired('phoneNumber', $this->phoneNumber, true);
        Model::validateRequired('smsCode', $this->smsCode, true);
        Model::validateRequired('smsCodeId', $this->smsCodeId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
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
     *
     * @return MobileRegisterRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['app_id'])) {
            $model->appId = $map['app_id'];
        }
        if (isset($map['nvc_param'])) {
            $model->nvcParam = $map['nvc_param'];
        }
        if (isset($map['phone_number'])) {
            $model->phoneNumber = $map['phone_number'];
        }
        if (isset($map['phone_region'])) {
            $model->phoneRegion = $map['phone_region'];
        }
        if (isset($map['sms_code'])) {
            $model->smsCode = $map['sms_code'];
        }
        if (isset($map['sms_code_id'])) {
            $model->smsCodeId = $map['sms_code_id'];
        }

        return $model;
    }
}
