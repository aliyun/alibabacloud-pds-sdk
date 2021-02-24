<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class GetMembershipRequest extends Model
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
     * @var string
     */
    public $memberType;

    /**
     * @var string
     */
    public $subGroupId;

    /**
     * @description subdomain id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504794"
     *
     * @var string
     */
    public $subdomainId;

    /**
     * @var string
     */
    public $userId;
    protected $_name = [
        'groupId'     => 'group_id',
        'memberType'  => 'member_type',
        'subGroupId'  => 'sub_group_id',
        'subdomainId' => 'subdomain_id',
        'userId'      => 'user_id',
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
        if (null !== $this->memberType) {
            $res['member_type'] = $this->memberType;
        }
        if (null !== $this->subGroupId) {
            $res['sub_group_id'] = $this->subGroupId;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetMembershipRequest
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
        if (isset($map['member_type'])) {
            $model->memberType = $map['member_type'];
        }
        if (isset($map['sub_group_id'])) {
            $model->subGroupId = $map['sub_group_id'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
