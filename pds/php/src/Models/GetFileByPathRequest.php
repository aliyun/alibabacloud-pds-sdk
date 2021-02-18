<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 根据路径获取 File 接口 body.
 */
class GetFileByPathRequest extends Model
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
     * @description file_path
     *
     * @example /a/b/c
     *
     * @var string
     */
    public $filePath;

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
     * @var string
     */
    public $referer;

    /**
     * @var string
     */
    public $signToken;

    /**
     * @description url_expire_sec
     *
     * @example 900
     *
     * @var int
     */
    public $urlExpireSec;

    /**
     * @description video_thumbnail_process
     * type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     *
     * @var string
     */
    public $videoThumbnailProcess;
    protected $_name = [
        'additionData'              => 'addition_data',
        'driveId'                   => 'drive_id',
        'filePath'                  => 'file_path',
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess'     => 'image_thumbnail_process',
        'imageUrlProcess'           => 'image_url_process',
        'referer'                   => 'referer',
        'signToken'                 => 'sign_token',
        'urlExpireSec'              => 'url_expire_sec',
        'videoThumbnailProcess'     => 'video_thumbnail_process',
    ];
    protected $_default = [
        'urlExpireSec' => 900,
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('urlExpireSec', $this->urlExpireSec, 14400);
        Model::validateMinimum('urlExpireSec', $this->urlExpireSec, 10);
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
        if (null !== $this->filePath) {
            $res['file_path'] = $this->filePath;
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
        if (null !== $this->referer) {
            $res['referer'] = $this->referer;
        }
        if (null !== $this->signToken) {
            $res['sign_token'] = $this->signToken;
        }
        if (null !== $this->urlExpireSec) {
            $res['url_expire_sec'] = $this->urlExpireSec;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetFileByPathRequest
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
        if (isset($map['file_path'])) {
            $model->filePath = $map['file_path'];
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
        if (isset($map['referer'])) {
            $model->referer = $map['referer'];
        }
        if (isset($map['sign_token'])) {
            $model->signToken = $map['sign_token'];
        }
        if (isset($map['url_expire_sec'])) {
            $model->urlExpireSec = $map['url_expire_sec'];
        }
        if (isset($map['video_thumbnail_process'])) {
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }

        return $model;
    }
}
