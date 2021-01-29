<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Base user response
 */
class BaseUserResponse extends Model {
    protected $_name = [
        'avatar' => 'avatar',
        'createdAt' => 'created_at',
        'defaultDriveId' => 'default_drive_id',
        'description' => 'description',
        'domainId' => 'domain_id',
        'email' => 'email',
        'nickName' => 'nick_name',
        'phone' => 'phone',
        'role' => 'role',
        'status' => 'status',
        'updatedAt' => 'updated_at',
        'userData' => 'user_data',
        'userId' => 'user_id',
        'userName' => 'user_name',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->avatar) {
            $res['avatar'] = $this->avatar;
        }
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->defaultDriveId) {
            $res['default_drive_id'] = $this->defaultDriveId;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->email) {
            $res['email'] = $this->email;
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
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
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
     * @return BaseUserResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['avatar'])){
            $model->avatar = $map['avatar'];
        }
        if(isset($map['created_at'])){
            $model->createdAt = $map['created_at'];
        }
        if(isset($map['default_drive_id'])){
            $model->defaultDriveId = $map['default_drive_id'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        if(isset($map['email'])){
            $model->email = $map['email'];
        }
        if(isset($map['nick_name'])){
            $model->nickName = $map['nick_name'];
        }
        if(isset($map['phone'])){
            $model->phone = $map['phone'];
        }
        if(isset($map['role'])){
            $model->role = $map['role'];
        }
        if(isset($map['status'])){
            $model->status = $map['status'];
        }
        if(isset($map['updated_at'])){
            $model->updatedAt = $map['updated_at'];
        }
        if(isset($map['user_data'])){
            $model->userData = $map['user_data'];
        }
        if(isset($map['user_id'])){
            $model->userId = $map['user_id'];
        }
        if(isset($map['user_name'])){
            $model->userName = $map['user_name'];
        }
        return $model;
    }
    /**
     * @description 头像
     * @example http://a.b.c/ccp.jpg
     * @var string
     */
    public $avatar;

    /**
     * @description 用户创建时间
     * @example 1567407718386
     * @var int
     */
    public $createdAt;

    /**
     * @description 默认 Drive ID
     * @example 123
     * @var string
     */
    public $defaultDriveId;

    /**
     * @description 用户备注信息
     * @example ccp team user
     * @var string
     */
    public $description;

    /**
     * @description Domain ID
     * @example hz999
     * @var string
     */
    public $domainId;

    /**
     * @description 邮箱
     * @example 123@ccp.com
     * @var string
     */
    public $email;

    /**
     * @description 昵称
     * @example abc
     * @var string
     */
    public $nickName;

    /**
     * @description 电话
     * @example 13700000000
     * @var string
     */
    public $phone;

    /**
     * @description 角色
     * @example user
     * @var string
     */
    public $role;

    /**
     * @description 用户状态
     * @example enabled
     * @var string
     */
    public $status;

    /**
     * @description 用户修改时间
     * @example 1567407718386
     * @var int
     */
    public $updatedAt;

    /**
     * @description 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
     * @example { is_student: true }
     * @var mixed[]
     */
    public $userData;

    /**
     * @description 用户 ID
     * @example ccpuserid
     * @var string
     */
    public $userId;

    /**
     * @description 用户名称
     * @example name
     * @var string
     */
    public $userName;

}
