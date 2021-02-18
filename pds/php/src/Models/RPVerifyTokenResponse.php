<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\VerifyTokenResponse;

/**
 * *
 */
class RPVerifyTokenResponse extends Model {
    protected $_name = [
        'needRpVerify' => 'need_rp_verify',
        'verifyToken' => 'verify_token',
    ];
    public function validate() {
        Model::validateRequired('needRpVerify', $this->needRpVerify, true);
        Model::validateRequired('verifyToken', $this->verifyToken, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->needRpVerify) {
            $res['need_rp_verify'] = $this->needRpVerify;
        }
        if (null !== $this->verifyToken) {
            $res['verify_token'] = null !== $this->verifyToken ? $this->verifyToken->toMap() : null;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return RPVerifyTokenResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['need_rp_verify'])){
            $model->needRpVerify = $map['need_rp_verify'];
        }
        if(isset($map['verify_token'])){
            $model->verifyToken = VerifyTokenResponse::fromMap($map['verify_token']);
        }
        return $model;
    }
    /**
     * @description 是否需要实人认证，如果用户已通过认证，或者未开启实人认证，返回false
     * @example false
     * @var bool
     */
    public $needRpVerify;

    /**
     * @var VerifyTokenResponse
     */
    public $verifyToken;

}
