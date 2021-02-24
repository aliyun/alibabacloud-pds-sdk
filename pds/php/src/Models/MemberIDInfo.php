<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class MemberIDInfo extends Model
{
    /**
     * @var string
     */
    public $memberType;

    /**
     * @var string
     */
    public $subGroupId;

    /**
     * @var string
     */
    public $userId;
    protected $_name = [
        'memberType' => 'member_type',
        'subGroupId' => 'sub_group_id',
        'userId'     => 'user_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->memberType) {
            $res['member_type'] = $this->memberType;
        }
        if (null !== $this->subGroupId) {
            $res['sub_group_id'] = $this->subGroupId;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return MemberIDInfo
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['member_type'])) {
            $model->memberType = $map['member_type'];
        }
        if (isset($map['sub_group_id'])) {
            $model->subGroupId = $map['sub_group_id'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
