<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CreateDetail extends Model
{
    /**
     * @description CreateType
     *
     * @var string
     */
    public $createType;

    /**
     * @description SrcFileID
     *
     * @var string
     */
    public $srcFileId;
    protected $_name = [
        'createType' => 'create_type',
        'srcFileId'  => 'src_file_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->createType) {
            $res['create_type'] = $this->createType;
        }
        if (null !== $this->srcFileId) {
            $res['src_file_id'] = $this->srcFileId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateDetail
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['create_type'])) {
            $model->createType = $map['create_type'];
        }
        if (isset($map['src_file_id'])) {
            $model->srcFileId = $map['src_file_id'];
        }

        return $model;
    }
}
