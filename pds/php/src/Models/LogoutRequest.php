<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class LogoutRequest extends Model {
    protected $_name = [
        'BackUrl' => 'BackUrl',
        'ClientID' => 'ClientID',
        'LoginType' => 'LoginType',
    ];
    public function validate() {
        Model::validateRequired('ClientID', $this->ClientID, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->BackUrl) {
            $res['BackUrl'] = $this->BackUrl;
        }
        if (null !== $this->ClientID) {
            $res['ClientID'] = $this->ClientID;
        }
        if (null !== $this->LoginType) {
            $res['LoginType'] = $this->LoginType;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return LogoutRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['BackUrl'])){
            $model->BackUrl = $map['BackUrl'];
        }
        if(isset($map['ClientID'])){
            $model->ClientID = $map['ClientID'];
        }
        if(isset($map['LoginType'])){
            $model->LoginType = $map['LoginType'];
        }
        return $model;
    }
    /**
     * @description 登出之后的跳转地址，默认跳转到App的域名下
     * @example https://app.com/home
     * @var string
     */
    public $BackUrl;

    /**
     * @description Client ID, 此处填写创建App时返回的AppID
     * @example aksjoiajsoias
     * @var string
     */
    public $ClientID;

    /**
     * @description 用户自定义字段，会在鉴权成功后的callback带回
     * @var string
     */
    public $LoginType;

}
