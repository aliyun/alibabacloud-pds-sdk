<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class LoginByCodeRequest extends Model {
    protected $_name = [
        'accessToken' => 'access_token',
        'appId' => 'app_id',
        'authCode' => 'auth_code',
        'type' => 'type',
    ];
    public function validate() {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('type', $this->type, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->accessToken) {
            $res['access_token'] = $this->accessToken;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->authCode) {
            $res['auth_code'] = $this->authCode;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return LoginByCodeRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['access_token'])){
            $model->accessToken = $map['access_token'];
        }
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['auth_code'])){
            $model->authCode = $map['auth_code'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
        }
        return $model;
    }
    /**
     * @description 鉴权后返回的accessToken，淘宝登录需要此字段
     * @example csaklidwasdhjwid
     * @var string
     */
    public $accessToken;

    /**
     * @description App ID, 当前访问的App
     * @example csaklidwasdhjwid
     * @var string
     */
    public $appId;

    /**
     * @description 鉴权后返回的AuthCode，支付宝登录需要此字段
     * @example csaklidwasdhjwid
     * @var string
     */
    public $authCode;

    /**
     * @description 鉴权类型，淘宝、支付宝
     * @example taobao
     * @var string
     */
    public $type;

}
