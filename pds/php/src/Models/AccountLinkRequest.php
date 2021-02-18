<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class AccountLinkRequest extends Model
{
    public $headers;

    /**
     * @description 账号信息
     *
     * @example {name:jack,age:20}
     *
     * @var string
     */
    public $detail;

    /**
     * @description 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
     *
     * @example 1
     *
     * @var string
     */
    public $extra;

    /**
     * @description 唯一身份标识
     *
     * @example 15208333333
     *
     * @var string
     */
    public $identity;

    /**
     * @description 状态
     *
     * @example normal
     *
     * @var string
     */
    public $status;

    /**
     * @description 认证类型
     *
     * @example mobile
     *
     * @var string
     */
    public $type;

    /**
     * @description 绑定的user_id
     *
     * @example 123987123617823
     *
     * @var string
     */
    public $userId;
    protected $_name = [
        'detail'   => 'detail',
        'extra'    => 'extra',
        'identity' => 'identity',
        'status'   => 'status',
        'type'     => 'type',
        'userId'   => 'user_id',
    ];

    public function validate()
    {
        Model::validateRequired('identity', $this->identity, true);
        Model::validateRequired('type', $this->type, true);
        Model::validateRequired('userId', $this->userId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->detail) {
            $res['detail'] = $this->detail;
        }
        if (null !== $this->extra) {
            $res['extra'] = $this->extra;
        }
        if (null !== $this->identity) {
            $res['identity'] = $this->identity;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return AccountLinkRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['detail'])) {
            $model->detail = $map['detail'];
        }
        if (isset($map['extra'])) {
            $model->extra = $map['extra'];
        }
        if (isset($map['identity'])) {
            $model->identity = $map['identity'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
