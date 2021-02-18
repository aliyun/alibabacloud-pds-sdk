<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 列举uploadID对应的已上传分片.
 */
class HostingListUploadedPartRequest extends Model
{
    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description file_path
     *
     * @example /a/b/c.jpg
     *
     * @var string
     */
    public $filePath;

    /**
     * @description limit
     *
     * @example 1
     *
     * @var int
     */
    public $limit;

    /**
     * @description part_number_marker
     *
     * @example 1
     *
     * @var int
     */
    public $partNumberMarker;

    /**
     * @description share_id
     *
     * @example 3d336314-63c8-4d96-bce0-17aefb6833b6
     *
     * @var string
     */
    public $shareId;

    /**
     * @description upload_id
     *
     * @example 00668396C0814D818D90F0A92B04B355
     *
     * @var string
     */
    public $uploadId;
    protected $_name = [
        'driveId'          => 'drive_id',
        'filePath'         => 'file_path',
        'limit'            => 'limit',
        'partNumberMarker' => 'part_number_marker',
        'shareId'          => 'share_id',
        'uploadId'         => 'upload_id',
    ];
    protected $_default = [
        'limit' => 1000,
    ];

    public function validate()
    {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('shareId', $this->shareId, '[0-9a-zA-Z-]+');
        Model::validateRequired('filePath', $this->filePath, true);
        Model::validateMaximum('limit', $this->limit, 1000);
        Model::validateMinimum('limit', $this->limit, 1);
        Model::validateMinimum('partNumberMarker', $this->partNumberMarker, 1);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->filePath) {
            $res['file_path'] = $this->filePath;
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
     *
     * @return HostingListUploadedPartRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_path'])) {
            $model->filePath = $map['file_path'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['part_number_marker'])) {
            $model->partNumberMarker = $map['part_number_marker'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['upload_id'])) {
            $model->uploadId = $map['upload_id'];
        }

        return $model;
    }
}
