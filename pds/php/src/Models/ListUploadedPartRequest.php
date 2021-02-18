<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 列举uploadID对应的已上传分片
 */
class ListUploadedPartRequest extends Model {
    protected $_name = [
        'driveId' => 'drive_id',
        'fileId' => 'file_id',
        'fileIdPath' => 'file_id_path',
        'limit' => 'limit',
        'partNumberMarker' => 'part_number_marker',
        'shareId' => 'share_id',
        'uploadId' => 'upload_id',
    ];
    protected $_default = [
        'limit' => 1000,
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMaximum('limit', $this->limit, 1000);
        Model::validateMinimum('limit', $this->limit, 1);
        Model::validateMinimum('partNumberMarker', $this->partNumberMarker, 1);
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
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->partNumberMarker) {
            $res['part_number_marker'] = $this->partNumberMarker;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->uploadId) {
            $res['upload_id'] = $this->uploadId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ListUploadedPartRequest
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
        if(isset($map['limit'])){
            $model->limit = $map['limit'];
        }
        if(isset($map['part_number_marker'])){
            $model->partNumberMarker = $map['part_number_marker'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['upload_id'])){
            $model->uploadId = $map['upload_id'];
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
     * @description limit
     * @example 1
     * @var int
     */
    public $limit;

    /**
     * @description part_number_marker
     * @example 1
     * @var int
     */
    public $partNumberMarker;

    /**
     * @var string
     */
    public $shareId;

    /**
     * @description upload_id
     * @example 00668396C0814D818D90F0A92B04B355
     * @var string
     */
    public $uploadId;

}
