<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ListAppsRequest extends Model
{
    /**
     * @description 返回结果数据
     *
     * @example 100
     *
     * @var int
     */
    public $limit;

    /**
     * @description 下次查询游标
     *
     * @example ncsajnsalsa=
     *
     * @var string
     */
    public $marker;
    protected $_name = [
        'limit'  => 'limit',
        'marker' => 'marker',
    ];
    protected $_default = [
        'limit' => 50,
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
     * @return ListAppsRequest
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
