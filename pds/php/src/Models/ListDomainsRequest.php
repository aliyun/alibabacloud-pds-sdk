<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list domain request.
 */
class ListDomainsRequest extends Model
{
    /**
     * @description 分页大小
     *
     * @example 100
     *
     * @var int
     */
    public $limit;

    /**
     * @description 查询游标
     *
     * @example abcd
     *
     * @var string
     */
    public $marker;
    protected $_name = [
        'limit'  => 'limit',
        'marker' => 'marker',
    ];

    public function validate()
    {
        Model::validateMaximum('limit', $this->limit, 100);
        Model::validateMinimum('limit', $this->limit, 1);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListDomainsRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }

        return $model;
    }
}
