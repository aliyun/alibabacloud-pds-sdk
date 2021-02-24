<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list_share_link request.
 */
class ListShareLinkRequest extends Model
{
    public $headers;

    /**
     * @description creator
     *
     * @example tom
     *
     * @var string
     */
    public $creator;

    /**
     * @description limit
     *
     * @example 50
     *
     * @var int
     */
    public $limit;

    /**
     * @description marker
     *
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     *
     * @var string
     */
    public $marker;

    /**
     * @description order_by
     *
     * @example share_name
     *
     * @var string
     */
    public $orderBy;

    /**
     * @description order_direction
     *
     * @example ASC
     *
     * @var string
     */
    public $orderDirection;
    protected $_name = [
        'creator'        => 'creator',
        'limit'          => 'limit',
        'marker'         => 'marker',
        'orderBy'        => 'order_by',
        'orderDirection' => 'order_direction',
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
        if (null !== $this->creator) {
            $res['creator'] = $this->creator;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->orderBy) {
            $res['order_by'] = $this->orderBy;
        }
        if (null !== $this->orderDirection) {
            $res['order_direction'] = $this->orderDirection;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListShareLinkRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['creator'])) {
            $model->creator = $map['creator'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }
        if (isset($map['order_by'])) {
            $model->orderBy = $map['order_by'];
        }
        if (isset($map['order_direction'])) {
            $model->orderDirection = $map['order_direction'];
        }

        return $model;
    }
}
