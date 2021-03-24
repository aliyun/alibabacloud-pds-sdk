<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class RenameDetail extends Model
{
    /**
     * @description NewName
     *
     * @var string
     */
    public $newName;

    /**
     * @description OldName
     *
     * @var string
     */
    public $oldName;
    protected $_name = [
        'newName' => 'new_name',
        'oldName' => 'old_name',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->newName) {
            $res['new_name'] = $this->newName;
        }
        if (null !== $this->oldName) {
            $res['old_name'] = $this->oldName;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return RenameDetail
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['new_name'])) {
            $model->newName = $map['new_name'];
        }
        if (isset($map['old_name'])) {
            $model->oldName = $map['old_name'];
        }

        return $model;
    }
}
