<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseFileProcessRequest extends Model
{
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
     * @description video_thumbnail_process
     * type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     *
     * @var string
     */
    public $videoThumbnailProcess;
    protected $_name = [
        'imageCroppingAspectRatios' => 'image_cropping_aspect_ratios',
        'imageThumbnailProcess'     => 'image_thumbnail_process',
        'imageUrlProcess'           => 'image_url_process',
        'videoThumbnailProcess'     => 'video_thumbnail_process',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->imageCroppingAspectRatios) {
            $res['image_cropping_aspect_ratios'] = $this->imageCroppingAspectRatios;
        }
        if (null !== $this->imageThumbnailProcess) {
            $res['image_thumbnail_process'] = $this->imageThumbnailProcess;
        }
        if (null !== $this->imageUrlProcess) {
            $res['image_url_process'] = $this->imageUrlProcess;
        }
        if (null !== $this->videoThumbnailProcess) {
            $res['video_thumbnail_process'] = $this->videoThumbnailProcess;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseFileProcessRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
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
        if (isset($map['video_thumbnail_process'])) {
            $model->videoThumbnailProcess = $map['video_thumbnail_process'];
        }

        return $model;
    }
}
