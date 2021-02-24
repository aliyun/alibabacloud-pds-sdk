<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ListDirectChildMembershipsRequest extends Model
{
    public $headers;

    /**
     * @description group id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504793"
     *
     * @var string
     */
    public $groupId;

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
     * @description 角色，可选值，["", "member", "admin"], ""表示获取所有类型
     *
     * @example "member"
     *
     * @var string
     */
    public $memberType;

    /**
     * @description subdomain id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504794"
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'groupId'     => 'group_id',
        'limit'       => 'limit',
        'marker'      => 'marker',
        'memberType'  => 'member_type',
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
        if (null !== $this->groupId) {
            $res['group_id'] = $this->groupId;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->marker) {
            $res['marker'] = $this->marker;
        }
        if (null !== $this->memberType) {
            $res['member_type'] = $this->memberType;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListDirectChildMembershipsRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['group_id'])) {
            $model->groupId = $map['group_id'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }
        if (isset($map['member_type'])) {
            $model->memberType = $map['member_type'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
