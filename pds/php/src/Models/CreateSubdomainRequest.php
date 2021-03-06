<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CreateSubdomainRequest extends Model
{
    public $headers;

    /**
     * @description 描述
     *
     * @example "描述-1"
     *
     * @var string
     */
    public $description;

    /**
     * @description 名称，注意该字段会校验重名的subdomain
     *
     * @example "subdomain-1"
     *
     * @var string
     */
    public $name;

    /**
     * @description 逻辑空间quota，默认为-1，无限制，单位为字节
     *
     * @example 1099511627776
     *
     * @var int
     */
    public $totalSize;

    /**
     * @description 用户数quota，默认为-1，无限制
     *
     * @example 100
     *
     * @var int
     */
    public $userQuota;
    protected $_name = [
        'description' => 'description',
        'name'        => 'name',
        'totalSize'   => 'total_size',
        'userQuota'   => 'user_quota',
    ];

    public function validate()
    {
        Model::validateRequired('name', $this->name, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->totalSize) {
            $res['total_size'] = $this->totalSize;
        }
        if (null !== $this->userQuota) {
            $res['user_quota'] = $this->userQuota;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateSubdomainRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['name'])) {
            $model->name = $map['name'];
        }
        if (isset($map['total_size'])) {
            $model->totalSize = $map['total_size'];
        }
        if (isset($map['user_quota'])) {
            $model->userQuota = $map['user_quota'];
        }

        return $model;
    }
}
