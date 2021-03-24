<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class TrashDetail extends Model
{
    /**
     * @description ParentFileID
     *
     * @var string
     */
    public $parentFileId;
    protected $_name = [
        'parentFileId' => 'parent_file_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->parentFileId) {
            $res['parent_file_id'] = $this->parentFileId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return TrashDetail
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['parent_file_id'])) {
            $model->parentFileId = $map['parent_file_id'];
        }

        return $model;
    }
}
