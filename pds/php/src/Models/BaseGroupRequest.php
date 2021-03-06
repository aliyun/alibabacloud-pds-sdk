<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseGroupRequest extends Model
{
    /**
     * @description 描述
     *
     * @example "desc-1"
     *
     * @var string
     */
    public $description;

    /**
     * @description 名称
     *
     * @example "group-1"
     *
     * @var string
     */
    public $groupName;

    /**
     * @description 是否是根group
     *
     * @example false
     *
     * @var bool
     */
    public $isRoot;
    protected $_name = [
        'description' => 'description',
        'groupName'   => 'group_name',
        'isRoot'      => 'is_root',
    ];

    public function validate()
    {
        Model::validateRequired('groupName', $this->groupName, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->groupName) {
            $res['group_name'] = $this->groupName;
        }
        if (null !== $this->isRoot) {
            $res['is_root'] = $this->isRoot;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseGroupRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['group_name'])) {
            $model->groupName = $map['group_name'];
        }
        if (isset($map['is_root'])) {
            $model->isRoot = $map['is_root'];
        }

        return $model;
    }
}
