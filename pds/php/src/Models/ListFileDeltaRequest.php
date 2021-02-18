<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取增量文件操作记录.
 */
class ListFileDeltaRequest extends Model
{
    public $headers;

    /**
     * @description cursor 游标
     *
     * @example abc
     *
     * @var string
     */
    public $cursor;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @example 1:1, 1:2, 2:1, 2:3, 3:2, 7:4
     *
     * @var string[]
     */
    public $imageCroppingAspectRatios;

    /**
     * @description image_thumbnail_process
     *
     * @example image/resize,w_200
     *
     * @var string
     */
    public $imageThumbnailProcess;

    /**
     * @description image_url_process
     *
     * @example image/resize,w_200
     *
     * @var string
     */
    public $imageUrlProcess;

    /**
     * @description limit
     * default 100
     * @example 100
     *
     * @var int
     */
    public $limit;

    /**
     * @description video_thumbnail_process
     * type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     *
     * @var string
     */
    public $videoThumbnailProcess;
    protected $_name = [
        'cursor'                    => 'cursor',
        'driveId'                   => 'drive_id',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess'     => 'image_thumbnail_process',
        'imageUrlProcess'           => 'image_url_process',
        'limit'                     => 'limit',
        'videoThumbnailProcess'     => 'video_thumbnail_process',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->cursor) {
            $res['cursor'] = $this->cursor;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->imageCroppingAspectRatios) {
            $res['image_cropping_aspect_ratios'] = $this->imageCroppingAspectRatios;
        }
        if (null !== $this->imageThumbnailProcess) {
            $res['image_thumbnail_process'] = $this->imageThumbnailProcess;
        }
        if (null !== $this->imageUrlProcess) {
            $res['image_url_process'] = $this->imageUrlProcess;
        }
        if (null !== $this->limit) {
            $res['limit'] = $this->limit;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ListFileDeltaRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['cursor'])) {
            $model->cursor = $map['cursor'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['image_cropping_aspect_ratios'])) {
            if (!empty($map['image_cropping_aspect_ratios'])) {
                $model->imageCroppingAspectRatios = $map['image_cropping_aspect_ratios'];
            }
        }
        if (isset($map['image_thumbnail_process'])) {
            $model->imageThumbnailProcess = $map['image_thumbnail_process'];
        }
        if (isset($map['image_url_process'])) {
            $model->imageUrlProcess = $map['image_url_process'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['video_thumbnail_process'])) {
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }

        return $model;
    }
}
