<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 文件拷贝
 */
class CopyFileRequest extends Model {
    protected $_name = [
        'autoRename' => 'auto_rename',
        'driveId' => 'drive_id',
        'fileId' => 'file_id',
        'fileIdPath' => 'file_id_path',
        'newName' => 'new_name',
        'shareId' => 'share_id',
        'toDriveId' => 'to_drive_id',
        'toParentFileId' => 'to_parent_file_id',
        'toShareId' => 'to_share_id',
    ];
    protected $_default = [
        'autoRename' => 'false',
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validatePattern('toDriveId', $this->toDriveId, '[0-9]+');
        Model::validatePattern('toParentFileId', $this->toParentFileId, '[a-z0-9.-_]{1,50}');
        Model::validatePattern('toShareId', $this->toShareId, '[0-9]+');
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validateRequired('toParentFileId', $this->toParentFileId, true);
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMaxLength('newName', $this->newName, 1024);
        Model::validateMaxLength('toParentFileId', $this->toParentFileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMinLength('newName', $this->newName, 1);
        Model::validateMinLength('toParentFileId', $this->toParentFileId, 4);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->autoRename) {
            $res['auto_rename'] = $this->autoRename;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileIdPath) {
            $res['file_id_path'] = $this->fileIdPath;
        }
        if (null !== $this->newName) {
            $res['new_name'] = $this->newName;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->toDriveId) {
            $res['to_drive_id'] = $this->toDriveId;
        }
        if (null !== $this->toParentFileId) {
            $res['to_parent_file_id'] = $this->toParentFileId;
        }
        if (null !== $this->toShareId) {
            $res['to_share_id'] = $this->toShareId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return CopyFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['auto_rename'])){
            $model->autoRename = $map['auto_rename'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['file_id_path'])){
            $model->fileIdPath = $map['file_id_path'];
        }
        if(isset($map['new_name'])){
            $model->newName = $map['new_name'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['to_drive_id'])){
            $model->toDriveId = $map['to_drive_id'];
        }
        if(isset($map['to_parent_file_id'])){
            $model->toParentFileId = $map['to_parent_file_id'];
        }
        if(isset($map['to_share_id'])){
            $model->toShareId = $map['to_share_id'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description auto_rename
type: boolean
     * @example false
     * @var bool
     */
    public $autoRename;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description file_id
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     * @var string
     */
    public $fileId;

    /**
     * @var string
     */
    public $fileIdPath;

    /**
     * @description new_name
     * @example ccp.jpg
     * @var string
     */
    public $newName;

    /**
     * @description share_id, either share_id or drive_id is required
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     * @var string
     */
    public $shareId;

    /**
     * @description to_drive_id
     * @example 1
     * @var string
     */
    public $toDriveId;

    /**
     * @description to_parent_file_id
     * @example root
     * @var string
     */
    public $toParentFileId;

    /**
     * @description to_drive_id
     * @example 1
     * @var string
     */
    public $toShareId;

}
