<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Search user request
 */
class SearchUserRequest extends Model {
    protected $_name = [
        'email' => 'email',
        'limit' => 'limit',
        'marker' => 'marker',
        'nickName' => 'nick_name',
        'phone' => 'phone',
        'role' => 'role',
        'status' => 'status',
        'userName' => 'user_name',
    ];
    protected $_default = [
        'limit' => 100,
        'role' => 'user',
        'status' => 'enabled',
    ];
    public function validate() {
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMinimum('limit', $this->limit, 1);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->email) {
            $res['email'] = $this->email;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
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
        if (null !== $this->userName) {
            $res['user_name'] = $this->userName;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return SearchUserRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['email'])){
            $model->email = $map['email'];
        }
        if(isset($map['limit'])){
            $model->limit = $map['limit'];
        }
        if(isset($map['marker'])){
            $model->marker = $map['marker'];
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
        if(isset($map['user_name'])){
            $model->userName = $map['user_name'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description 邮箱
     * @example abc@ccp.com
     * @var string
     */
    public $email;

    /**
     * @description 每页大小限制
     * @example 10
     * @var int
     */
    public $limit;

    /**
     * @description 翻页标记
     * @example marker
     * @var string
     */
    public $marker;

    /**
     * @description 昵称
     * @example la
     * @var string
     */
    public $nickName;

    /**
     * @description 电话号码
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
     * @description 状态
     * @example enabled
     * @var string
     */
    public $status;

    /**
     * @description 用户名
     * @example abc
     * @var string
     */
    public $userName;

}
