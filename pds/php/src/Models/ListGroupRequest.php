<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ListGroupRequest extends Model
{
    public $headers;

    /**
     * @description 分页获取的数量，默认为100
     *
     * @example 10
     *
     * @var int
     */
    public $limit;

    /**
     * @description 游标
     *
     * @example ""
     *
     * @var string
     */
    public $marker;

    /**
     * @description 列举 subdomain 下的group
     *
     * @example "b38b5681bd964950ad8bc0f8ea504793"
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'limit'       => 'limit',
        'marker'      => 'marker',
        'subdomainId' => 'subdomain_id',
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
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListGroupRequest
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
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
