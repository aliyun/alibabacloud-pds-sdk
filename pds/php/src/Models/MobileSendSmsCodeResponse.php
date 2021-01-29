<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class MobileSendSmsCodeResponse extends Model {
    protected $_name = [
        'smsCodeId' => 'sms_code_id',
    ];
    public function validate() {
        Model::validateRequired('smsCodeId', $this->smsCodeId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->smsCodeId) {
            $res['sms_code_id'] = $this->smsCodeId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return MobileSendSmsCodeResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['sms_code_id'])){
            $model->smsCodeId = $map['sms_code_id'];
        }
        return $model;
    }
    /**
     * @description 短信验证码ID
     * @example csjanwia
     * @var string
     */
    public $smsCodeId;

}
