<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class MoveDetail extends Model
{
    /**
     * @description SrcParentFileID
     *
     * @var string
     */
    public $srcParentFileId;

    /**
     * @description TgtParentFileID
     *
     * @var string
     */
    public $tgtParentFileId;
    protected $_name = [
        'srcParentFileId' => 'src_parent_file_id',
        'tgtParentFileId' => 'tgt_parent_file_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->srcParentFileId) {
            $res['src_parent_file_id'] = $this->srcParentFileId;
        }
        if (null !== $this->tgtParentFileId) {
            $res['tgt_parent_file_id'] = $this->tgtParentFileId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return MoveDetail
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['src_parent_file_id'])) {
            $model->srcParentFileId = $map['src_parent_file_id'];
        }
        if (isset($map['tgt_parent_file_id'])) {
            $model->tgtParentFileId = $map['tgt_parent_file_id'];
        }

        return $model;
    }
}
