<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 删除文件请求
 */
class DeleteFileRequest extends Model {
    protected $_name = [
        'driveId' => 'drive_id',
        'fileId' => 'file_id',
        'fileIdPath' => 'file_id_path',
        'permanently' => 'permanently',
        'shareId' => 'share_id',
    ];
    protected $_default = [
        'permanently' => 'false',
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
    }
    public function toMap() {
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
        if (null !== $this->fileIdPath) {
            $res['file_id_path'] = $this->fileIdPath;
        }
        if (null !== $this->permanently) {
            $res['permanently'] = $this->permanently;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return DeleteFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
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
        if(isset($map['permanently'])){
            $model->permanently = $map['permanently'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @var string
     */
    public $fileId;

    /**
     * @var string
     */
    public $fileIdPath;

    /**
     * @description permanently
type: false
     * @example false
     * @var bool
     */
    public $permanently;

    /**
     * @var string
     */
    public $shareId;

}
