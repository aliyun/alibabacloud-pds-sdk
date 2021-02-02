<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class AccountTokenRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'appId' => 'app_id',
        'grantType' => 'grant_type',
        'refreshToken' => 'refresh_token',
    ];
    public function validate() {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('grantType', $this->grantType, true);
        Model::validateRequired('refreshToken', $this->refreshToken, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->grantType) {
            $res['grant_type'] = $this->grantType;
        }
        if (null !== $this->refreshToken) {
            $res['refresh_token'] = $this->refreshToken;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return AccountTokenRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['app_id'])){
            $model->appId = $map['app_id'];
        }
        if(isset($map['grant_type'])){
            $model->grantType = $map['grant_type'];
        }
        if(isset($map['refresh_token'])){
            $model->refreshToken = $map['refresh_token'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description App ID, 当前访问的App
     * @example csaklidwasdhjwid
     * @var string
     */
    public $appId;

    /**
     * @description 只能填refresh_token
     * @example refresh_token
     * @var string
     */
    public $grantType;

    /**
     * @description refresh token, 登录时返回的
     * @example ybb3WJy2CwXHoM6hBcydGlvzMoJkFpkk
     * @var string
     */
    public $refreshToken;

}
