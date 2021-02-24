<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseMembershipResponse extends Model
{
    /**
     * @description created_at
     *
     * @example 1111
     *
     * @var int
     */
    public $createdAt;

    /**
     * @description 描述
     *
     * @example "desc-111"
     *
     * @var string
     */
    public $description;

    /**
     * @description domain id
     *
     * @example "bj123"
     *
     * @var string
     */
    public $domainId;

    /**
     * @description group id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504793"
     *
     * @var string
     */
    public $groupId;

    /**
     * @description 角色， member or admin
     *
     * @example "member"
     *
     * @var string
     */
    public $memberRole;

    /**
     * @var string
     */
    public $memberType;

    /**
     * @var string
     */
    public $subGroupId;

    /**
     * @description updated_at
     *
     * @example 1111
     *
     * @var int
     */
    public $updatedAt;

    /**
     * @var string
     */
    public $userId;
    protected $_name = [
        'createdAt'   => 'created_at',
        'description' => 'description',
        'domainId'    => 'domain_id',
        'groupId'     => 'group_id',
        'memberRole'  => 'member_role',
        'memberType'  => 'member_type',
        'subGroupId'  => 'sub_group_id',
        'updatedAt'   => 'updated_at',
        'userId'      => 'user_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->groupId) {
            $res['group_id'] = $this->groupId;
        }
        if (null !== $this->memberRole) {
            $res['member_role'] = $this->memberRole;
        }
        if (null !== $this->memberType) {
            $res['member_type'] = $this->memberType;
        }
        if (null !== $this->subGroupId) {
            $res['sub_group_id'] = $this->subGroupId;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseMembershipResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['created_at'])) {
            $model->createdAt = $map['created_at'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['group_id'])) {
            $model->groupId = $map['group_id'];
        }
        if (isset($map['member_role'])) {
            $model->memberRole = $map['member_role'];
        }
        if (isset($map['member_type'])) {
            $model->memberType = $map['member_type'];
        }
        if (isset($map['sub_group_id'])) {
            $model->subGroupId = $map['sub_group_id'];
        }
        if (isset($map['updated_at'])) {
            $model->updatedAt = $map['updated_at'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
