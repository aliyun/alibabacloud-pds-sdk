<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class VerifyTokenResponse extends Model {
    protected $_name = [
        'token' => 'token',
        'ttl' => 'ttl',
        'url' => 'url',
    ];
    public function validate() {
        Model::validateRequired('token', $this->token, true);
        Model::validateRequired('ttl', $this->ttl, true);
        Model::validateRequired('url', $this->url, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->token) {
            $res['token'] = $this->token;
        }
        if (null !== $this->ttl) {
            $res['ttl'] = $this->ttl;
        }
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return VerifyTokenResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['token'])){
            $model->token = $map['token'];
        }
        if(isset($map['ttl'])){
            $model->ttl = $map['ttl'];
        }
        if(isset($map['url'])){
            $model->url = $map['url'];
        }
        return $model;
    }
    /**
     * @description 实人认证的Token
     * @example "a5**d4"
     * @var string
     */
    public $token;

    /**
     * @description 实人认证token有效秒数，如1800
     * @example 1800
     * @var int
     */
    public $ttl;

    /**
     * @description 实人认证的URL，包含Token
     * @example "http://domain/router/?key=value&token=token_value"
     * @var string
     */
    public $url;

}
