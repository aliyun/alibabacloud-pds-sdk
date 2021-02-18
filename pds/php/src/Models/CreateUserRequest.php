<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Create user request.
 */
class CreateUserRequest extends Model
{
    public $headers;

    /**
     * @description 头像
     *
     * @example http://a.b.c/ccp.jpg
     *
     * @var string
     */
    public $avatar;

    /**
     * @description 描述信息
     *
     * @example ccp team user
     *
     * @var string
     */
    public $description;

    /**
     * @description 邮箱
     *
     * @example 123@ccp.com
     *
     * @var string
     */
    public $email;

    /**
     * @description 用户地域
     *
     * @var string
     */
    public $location;

    /**
     * @description 昵称
     *
     * @example ccpuser
     *
     * @var string
     */
    public $nickName;

    /**
     * @description 电话号码
     *
     * @example 13700000000
     *
     * @var string
     */
    public $phone;

    /**
     * @description 角色
     *
     * @example user
     *
     * @var string
     */
    public $role;

    /**
     * @description 状态
     *
     * @example enabled
     *
     * @var string
     */
    public $status;

    /**
     * @description 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
     *
     * @example { is_student: true }
     *
     * @var mixed[]
     */
    public $userData;

    /**
     * @description 用户 ID
     *
     * @example ccpuserid
     *
     * @var string
     */
    public $userId;

    /**
     * @description 用户名称
     *
     * @example abc
     *
     * @var string
     */
    public $userName;
    protected $_name = [
        'avatar'      => 'avatar',
        'description' => 'description',
        'email'       => 'email',
        'location'    => 'location',
        'nickName'    => 'nick_name',
        'phone'       => 'phone',
        'role'        => 'role',
        'status'      => 'status',
        'userData'    => 'user_data',
        'userId'      => 'user_id',
        'userName'    => 'user_name',
    ];
    protected $_default = [
        'role'   => 'user',
        'status' => 'enabled',
    ];

    public function validate()
    {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateRequired('userId', $this->userId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->avatar) {
            $res['avatar'] = $this->avatar;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->email) {
            $res['email'] = $this->email;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->nickName) {
            $res['nick_name'] = $this->nickName;
        }
        if (null !== $this->phone) {
            $res['phone'] = $this->phone;
        }
        if (null !== $this->role) {
            $res['role'] = $this->role;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
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
     * @return CreateUserRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['avatar'])) {
            $model->avatar = $map['avatar'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['email'])) {
            $model->email = $map['email'];
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }
        if (isset($map['nick_name'])) {
            $model->nickName = $map['nick_name'];
        }
        if (isset($map['phone'])) {
            $model->phone = $map['phone'];
        }
        if (isset($map['role'])) {
            $model->role = $map['role'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
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
