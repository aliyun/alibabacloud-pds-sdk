<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * List drive request.
 */
class ListDriveRequest extends Model
{
    public $headers;

    /**
     * @description 每页大小限制
     *
     * @example 10
     *
     * @var int
     */
    public $limit;

    /**
     * @description 翻页标记, 接口返回的标记值
     *
     * @example marker
     *
     * @var string
     */
    public $marker;

    /**
     * @description 所属者
     *
     * @example abc
     *
     * @var string
     */
    public $owner;
    protected $_name = [
        'limit'  => 'limit',
        'marker' => 'marker',
        'owner'  => 'owner',
    ];
    protected $_default = [
        'limit' => 100,
    ];

    public function validate()
    {
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMinimum('limit', $this->limit, 1);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->owner) {
            $res['owner'] = $this->owner;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListDriveRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }
        if (isset($map['owner'])) {
            $model->owner = $map['owner'];
        }

        return $model;
    }
}
