<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class AccountAccessTokenResponse extends Model
{
    /**
     * @description 用于调用业务接口的accessToken
     *
     * @example cnskjajkahwdhwialsnd
     *
     * @var string
     */
    public $accessToken;

    /**
     * @description 当前用户头像
     *
     * @example cherry
     *
     * @var string
     */
    public $avatar;

    /**
     * @description Default Drive ID
     *
     * @example 100
     *
     * @var string
     */
    public $defaultDriveId;

    /**
     * @description Default Sbox Drive ID
     *
     * @example 100
     *
     * @var string
     */
    public $defaultSboxDriveId;

    /**
     * @description device_id 通过device flow 绑定的设备ID
     *
     * @example xxx
     *
     * @var string
     */
    public $deviceId;

    /**
     * @description device_name 通过device flow 绑定的设备名
     *
     * @example xxx
     *
     * @var string
     */
    public $deviceName;

    /**
     * @description 当前用户已存在的登录方式
     *
     * @example
     *
     * @var LinkInfo[]
     */
    public $existLink;

    /**
     * @description accessToken过期时间，ISO时间
     *
     * @example 2019-09-01T06:57:48.813Z
     *
     * @var string
     */
    public $expireTime;

    /**
     * @description accessToken过期时间，单位秒
     *
     * @example 3600
     *
     * @var int
     */
    public $expiresIn;

    /**
     * @description 用户是否为第一次登录
     *
     * @example true
     *
     * @var bool
     */
    public $isFirstLogin;

    /**
     * @description 是否需要绑定
     *
     * @example false
     *
     * @var bool
     */
    public $needLink;

    /**
     * @description 用户是否需要进行的实人认证
     *
     * @example true
     *
     * @var bool
     */
    public $needRpVerify;

    /**
     * @description 当前用户昵称
     *
     * @example cherry
     *
     * @var string
     */
    public $nickName;

    /**
     * @description 用户的数据密码是否设置过
     *
     * @example true
     *
     * @var bool
     */
    public $pinSetup;

    /**
     * @description 用于刷新accessToken
     *
     * @example cnskjajkahwdhwialsnd
     *
     * @var string
     */
    public $refreshToken;

    /**
     * @description 当前用户角色
     *
     * @example user
     *
     * @var string
     */
    public $role;

    /**
     * @description 临时权限，用于登录成功后设置密码
     *
     * @example klafhjas-asdasd-asd-as-d-asd-asd-asdasd
     *
     * @var string
     */
    public $state;

    /**
     * @description 当前用户状态
     *
     * @example enabled
     *
     * @var string
     */
    public $status;

    /**
     * @description subdomain_id 用户登录的subdomain_id
     *
     * @example xxx
     *
     * @var string
     */
    public $subdomainId;

    /**
     * @description accessToken类型，Bearer
     *
     * @example Bearer
     *
     * @var string
     */
    public $tokenType;

    /**
     * @description 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
     *
     * @example { is_student: true }
     *
     * @var mixed[]
     */
    public $userData;

    /**
     * @description 当前用户ID
     *
     * @example DING-xxxxx
     *
     * @var string
     */
    public $userId;

    /**
     * @description 当前用户名
     *
     * @example cherry
     *
     * @var string
     */
    public $userName;
    protected $_name = [
        'accessToken'        => 'access_token',
        'avatar'             => 'avatar',
        'defaultDriveId'     => 'default_drive_id',
        'defaultSboxDriveId' => 'default_sbox_drive_id',
        'deviceId'           => 'device_id',
        'deviceName'         => 'device_name',
        'existLink'          => 'exist_link',
        'expireTime'         => 'expire_time',
        'expiresIn'          => 'expires_in',
        'isFirstLogin'       => 'is_first_login',
        'needLink'           => 'need_link',
        'needRpVerify'       => 'need_rp_verify',
        'nickName'           => 'nick_name',
        'pinSetup'           => 'pin_setup',
        'refreshToken'       => 'refresh_token',
        'role'               => 'role',
        'state'              => 'state',
        'status'             => 'status',
        'subdomainId'        => 'subdomain_id',
        'tokenType'          => 'token_type',
        'userData'           => 'user_data',
        'userId'             => 'user_id',
        'userName'           => 'user_name',
    ];

    public function validate()
    {
        Model::validateRequired('accessToken', $this->accessToken, true);
        Model::validateRequired('needLink', $this->needLink, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->accessToken) {
            $res['access_token'] = $this->accessToken;
        }
        if (null !== $this->avatar) {
            $res['avatar'] = $this->avatar;
        }
        if (null !== $this->defaultDriveId) {
            $res['default_drive_id'] = $this->defaultDriveId;
        }
        if (null !== $this->defaultSboxDriveId) {
            $res['default_sbox_drive_id'] = $this->defaultSboxDriveId;
        }
        if (null !== $this->deviceId) {
            $res['device_id'] = $this->deviceId;
        }
        if (null !== $this->deviceName) {
            $res['device_name'] = $this->deviceName;
        }
        if (null !== $this->existLink) {
            $res['exist_link'] = [];
            if (null !== $this->existLink && \is_array($this->existLink)) {
                $n = 0;
                foreach ($this->existLink as $item) {
                    $res['exist_link'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->expireTime) {
            $res['expire_time'] = $this->expireTime;
        }
        if (null !== $this->expiresIn) {
            $res['expires_in'] = $this->expiresIn;
        }
        if (null !== $this->isFirstLogin) {
            $res['is_first_login'] = $this->isFirstLogin;
        }
        if (null !== $this->needLink) {
            $res['need_link'] = $this->needLink;
        }
        if (null !== $this->needRpVerify) {
            $res['need_rp_verify'] = $this->needRpVerify;
        }
        if (null !== $this->nickName) {
            $res['nick_name'] = $this->nickName;
        }
        if (null !== $this->pinSetup) {
            $res['pin_setup'] = $this->pinSetup;
        }
        if (null !== $this->refreshToken) {
            $res['refresh_token'] = $this->refreshToken;
        }
        if (null !== $this->role) {
            $res['role'] = $this->role;
        }
        if (null !== $this->state) {
            $res['state'] = $this->state;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }
        if (null !== $this->tokenType) {
            $res['token_type'] = $this->tokenType;
        }
        if (null !== $this->userData) {
            $res['user_data'] = $this->userData;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }
        if (null !== $this->userName) {
            $res['user_name'] = $this->userName;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return AccountAccessTokenResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['access_token'])) {
            $model->accessToken = $map['access_token'];
        }
        if (isset($map['avatar'])) {
            $model->avatar = $map['avatar'];
        }
        if (isset($map['default_drive_id'])) {
            $model->defaultDriveId = $map['default_drive_id'];
        }
        if (isset($map['default_sbox_drive_id'])) {
            $model->defaultSboxDriveId = $map['default_sbox_drive_id'];
        }
        if (isset($map['device_id'])) {
            $model->deviceId = $map['device_id'];
        }
        if (isset($map['device_name'])) {
            $model->deviceName = $map['device_name'];
        }
        if (isset($map['exist_link'])) {
            if (!empty($map['exist_link'])) {
                $model->existLink = [];
                $n                = 0;
                foreach ($map['exist_link'] as $item) {
                    $model->existLink[$n++] = null !== $item ? LinkInfo::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['expire_time'])) {
            $model->expireTime = $map['expire_time'];
        }
        if (isset($map['expires_in'])) {
            $model->expiresIn = $map['expires_in'];
        }
        if (isset($map['is_first_login'])) {
            $model->isFirstLogin = $map['is_first_login'];
        }
        if (isset($map['need_link'])) {
            $model->needLink = $map['need_link'];
        }
        if (isset($map['need_rp_verify'])) {
            $model->needRpVerify = $map['need_rp_verify'];
        }
        if (isset($map['nick_name'])) {
            $model->nickName = $map['nick_name'];
        }
        if (isset($map['pin_setup'])) {
            $model->pinSetup = $map['pin_setup'];
        }
        if (isset($map['refresh_token'])) {
            $model->refreshToken = $map['refresh_token'];
        }
        if (isset($map['role'])) {
            $model->role = $map['role'];
        }
        if (isset($map['state'])) {
            $model->state = $map['state'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }
        if (isset($map['token_type'])) {
            $model->tokenType = $map['token_type'];
        }
        if (isset($map['user_data'])) {
            $model->userData = $map['user_data'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }
        if (isset($map['user_name'])) {
            $model->userName = $map['user_name'];
        }

        return $model;
    }
}
