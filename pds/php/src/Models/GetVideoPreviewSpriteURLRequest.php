<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取视频雪碧图地址的请求body.
 */
class GetVideoPreviewSpriteURLRequest extends Model
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
     * @description expire_sec
     *
     * @example 15
     *
     * @var int
     */
    public $expireSec;

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
        'driveId'   => 'drive_id',
        'expireSec' => 'expire_sec',
        'fileId'    => 'file_id',
        'shareId'   => 'share_id',
    ];
    protected $_default = [
        'expireSec' => 900,
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaximum('expireSec', $this->expireSec, 14400);
        Model::validateMinimum('expireSec', $this->expireSec, 1);
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
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
        if (null !== $this->expireSec) {
            $res['expire_sec'] = $this->expireSec;
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
     * @return GetVideoPreviewSpriteURLRequest
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
        if (isset($map['expire_sec'])) {
            $model->expireSec = $map['expire_sec'];
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
