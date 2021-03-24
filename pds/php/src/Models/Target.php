<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class Target extends Model
{
    /**
     * @description FileID
     *
     * @example ""
     *
     * @var string
     */
    public $fileId;

    /**
     * @description FileName
     *
     * @example ""
     *
     * @var string
     */
    public $fileName;

    /**
     * @description FileType
     *
     * @example ""
     *
     * @var string
     */
    public $fileType;
    protected $_name = [
        'fileId'   => 'file_id',
        'fileName' => 'file_name',
        'fileType' => 'file_type',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileName) {
            $res['file_name'] = $this->fileName;
        }
        if (null !== $this->fileType) {
            $res['file_type'] = $this->fileType;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return Target
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['file_name'])) {
            $model->fileName = $map['file_name'];
        }
        if (isset($map['file_type'])) {
            $model->fileType = $map['file_type'];
        }

        return $model;
    }
}
