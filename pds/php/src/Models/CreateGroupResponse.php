<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CreateGroupResponse extends Model
{
    /**
     * @description created_at
     *
     * @example 111111
     *
     * @var int
     */
    public $createdAt;

    /**
     * @description description
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
     * @description group name
     *
     * @example "name-111"
     *
     * @var string
     */
    public $groupName;

    /**
     * @description updated_at
     *
     * @example 111111
     *
     * @var int
     */
    public $updatedAt;
    protected $_name = [
        'createdAt'   => 'created_at',
        'description' => 'description',
        'domainId'    => 'domain_id',
        'groupId'     => 'group_id',
        'groupName'   => 'group_name',
        'updatedAt'   => 'updated_at',
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
        if (null !== $this->groupName) {
            $res['group_name'] = $this->groupName;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateGroupResponse
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
        if (isset($map['group_name'])) {
            $model->groupName = $map['group_name'];
        }
        if (isset($map['updated_at'])) {
            $model->updatedAt = $map['updated_at'];
        }

        return $model;
    }
}
