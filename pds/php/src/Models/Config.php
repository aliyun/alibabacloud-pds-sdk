<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class Config extends Model
{
    public $endpoint;

    /**
     * @var string
     */
    public $domainId;

    public $clientId;

    public $refreshToken;

    public $clientSecret;

    public $accessToken;

    public $expireTime;

    public $protocol;

    public $type;

    public $securityToken;

    public $accessKeyId;

    public $accessKeySecret;

    public $nickname;

    public $userAgent;

    public function validate()
    {
        Model::validatePattern('domainId', $this->domainId, '^[a-zA-Z0-9_-]+$');
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->endpoint) {
            $res['endpoint'] = $this->endpoint;
        }
        if (null !== $this->domainId) {
            $res['domainId'] = $this->domainId;
        }
        if (null !== $this->clientId) {
            $res['clientId'] = $this->clientId;
        }
        if (null !== $this->refreshToken) {
            $res['refreshToken'] = $this->refreshToken;
        }
        if (null !== $this->clientSecret) {
            $res['clientSecret'] = $this->clientSecret;
        }
        if (null !== $this->accessToken) {
            $res['accessToken'] = $this->accessToken;
        }
        if (null !== $this->expireTime) {
            $res['expireTime'] = $this->expireTime;
        }
        if (null !== $this->protocol) {
            $res['protocol'] = $this->protocol;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->securityToken) {
            $res['securityToken'] = $this->securityToken;
        }
        if (null !== $this->accessKeyId) {
            $res['accessKeyId'] = $this->accessKeyId;
        }
        if (null !== $this->accessKeySecret) {
            $res['accessKeySecret'] = $this->accessKeySecret;
        }
        if (null !== $this->nickname) {
            $res['nickname'] = $this->nickname;
        }
        if (null !== $this->userAgent) {
            $res['userAgent'] = $this->userAgent;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return Config
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['endpoint'])) {
            $model->endpoint = $map['endpoint'];
        }
        if (isset($map['domainId'])) {
            $model->domainId = $map['domainId'];
        }
        if (isset($map['clientId'])) {
            $model->clientId = $map['clientId'];
        }
        if (isset($map['refreshToken'])) {
            $model->refreshToken = $map['refreshToken'];
        }
        if (isset($map['clientSecret'])) {
            $model->clientSecret = $map['clientSecret'];
        }
        if (isset($map['accessToken'])) {
            $model->accessToken = $map['accessToken'];
        }
        if (isset($map['expireTime'])) {
            $model->expireTime = $map['expireTime'];
        }
        if (isset($map['protocol'])) {
            $model->protocol = $map['protocol'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }
        if (isset($map['securityToken'])) {
            $model->securityToken = $map['securityToken'];
        }
        if (isset($map['accessKeyId'])) {
            $model->accessKeyId = $map['accessKeyId'];
        }
        if (isset($map['accessKeySecret'])) {
            $model->accessKeySecret = $map['accessKeySecret'];
        }
        if (isset($map['nickname'])) {
            $model->nickname = $map['nickname'];
        }
        if (isset($map['userAgent'])) {
            $model->userAgent = $map['userAgent'];
        }

        return $model;
    }
}
