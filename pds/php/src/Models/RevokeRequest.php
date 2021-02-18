<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class RevokeRequest extends Model {
    protected $_name = [
        'appId' => 'app_id',
        'refreshToken' => 'refresh_token',
    ];
    public function validate() {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('refreshToken', $this->refreshToken, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->refreshToken) {
            $res['refresh_token'] = $this->refreshToken;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return RevokeRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['refresh_token'])){
            $model->refreshToken = $map['refresh_token'];
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
     * @description refresh token, 登录时返回的
     * @example ybb3WJy2CwXHoM6hBcydGlvzMoJkFpkk
     * @var string
     */
    public $refreshToken;

}
