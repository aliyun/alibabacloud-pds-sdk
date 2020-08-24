<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 文件移动请求
 */
class MoveFileRequest extends Model
{
    public $headers;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description file_id
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string
     */
    public $fileId;

    /**
     * @description new_name
     *
     * @example ccp.jpg
     *
     * @var string
     */
    public $newName;

    /**
     * @description overwrite
     * type: boolean
     * @example false
     *
     * @var bool
     */
    public $overwrite;

    /**
     * @description to_parent_file_id
     *
     * @example root
     *
     * @var string
     */
    public $toParentFileId;
    protected $_name = [
        'driveId'        => 'drive_id',
        'fileId'         => 'file_id',
        'newName'        => 'new_name',
        'overwrite'      => 'overwrite',
        'toParentFileId' => 'to_parent_file_id',
    ];
    protected $_default = [
        'overwrite' => 'false',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validateRequired('toParentFileId', $this->toParentFileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMaxLength('newName', $this->newName, 1024);
        Model::validateMaxLength('toParentFileId', $this->toParentFileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMinLength('newName', $this->newName, 1);
        Model::validateMinLength('toParentFileId', $this->toParentFileId, 4);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->newName) {
            $res['new_name'] = $this->newName;
        }
        if (null !== $this->overwrite) {
            $res['overwrite'] = $this->overwrite;
        }
        if (null !== $this->toParentFileId) {
            $res['to_parent_file_id'] = $this->toParentFileId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return MoveFileRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['new_name'])) {
            $model->newName = $map['new_name'];
        }
        if (isset($map['overwrite'])) {
            $model->overwrite = $map['overwrite'];
        }
        if (isset($map['to_parent_file_id'])) {
            $model->toParentFileId = $map['to_parent_file_id'];
        }

        return $model;
    }
}
