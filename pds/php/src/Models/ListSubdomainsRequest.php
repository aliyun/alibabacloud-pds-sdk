<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ListSubdomainsRequest extends Model
{
    public $headers;

    /**
     * @description 数量，默认为50
     *
     * @var int
     */
    public $limit;

    /**
     * @description 分页游标，可从 response 中获取
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

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListSubdomainsRequest
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

        return $model;
    }
}
