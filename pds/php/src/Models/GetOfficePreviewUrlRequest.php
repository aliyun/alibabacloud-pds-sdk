<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取office文档预览地址
 */
class GetOfficePreviewUrlRequest extends Model
{
    public $headers;

    /**
     * @description addition_data
     *
     * @var mixed[]
     */
    public $additionData;

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
     * @var string
     */
    public $fileId;

    /**
     * @description share_id, either share_id or drive_id is required
     *
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     *
     * @var string
     */
    public $shareId;
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId'      => 'drive_id',
        'fileId'       => 'file_id',
        'shareId'      => 'share_id',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetOfficePreviewUrlRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['addition_data'])) {
            $model->additionData = $map['addition_data'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }

        return $model;
    }
}
