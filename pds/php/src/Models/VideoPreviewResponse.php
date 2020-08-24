<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoPreviewResponse extends Model
{
    /**
     * @description audio_format
     *
     * @example "AAC"
     *
     * @var string
     */
    public $audioFormat;

    /**
     * @description bitrate
     *
     * @example "39101896"
     *
     * @var string
     */
    public $bitrate;

    /**
     * @description duration
     *
     * @example "8053"
     *
     * @var string
     */
    public $duration;

    /**
     * @description frame_rate
     *
     * @example "239.877"
     *
     * @var string
     */
    public $frameRate;

    /**
     * @description height
     *
     * @example 1280
     *
     * @var int
     */
    public $height;

    /**
     * @var VideoPreviewSprite
     */
    public $spriteInfo;

    /**
     * @description template_list
     *
     * @var array
     */
    public $templateList;

    /**
     * @description thumbnail
     *
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     *
     * @var string
     */
    public $thumbnail;

    /**
     * @description video_format
     *
     * @example "H264"
     *
     * @var string
     */
    public $videoFormat;

    /**
     * @description width
     *
     * @example 720
     *
     * @var int
     */
    public $width;
    protected $_name = [
        'audioFormat'  => 'audio_format',
        'bitrate'      => 'bitrate',
        'duration'     => 'duration',
        'frameRate'    => 'frame_rate',
        'height'       => 'height',
        'spriteInfo'   => 'sprite_info',
        'templateList' => 'template_list',
        'thumbnail'    => 'thumbnail',
        'videoFormat'  => 'video_format',
        'width'        => 'width',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->audioFormat) {
            $res['audio_format'] = $this->audioFormat;
        }
        if (null !== $this->bitrate) {
            $res['bitrate'] = $this->bitrate;
        }
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }
        if (null !== $this->frameRate) {
            $res['frame_rate'] = $this->frameRate;
        }
        if (null !== $this->height) {
            $res['height'] = $this->height;
        }
        if (null !== $this->spriteInfo) {
            $res['sprite_info'] = null !== $this->spriteInfo ? $this->spriteInfo->toMap() : null;
        }
        if (null !== $this->templateList) {
            $res['template_list'] = [];
            if (null !== $this->templateList && \is_array($this->templateList)) {
                $n = 0;
                foreach ($this->templateList as $item) {
                    $res['template_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->thumbnail) {
            $res['thumbnail'] = $this->thumbnail;
        }
        if (null !== $this->videoFormat) {
            $res['video_format'] = $this->videoFormat;
        }
        if (null !== $this->width) {
            $res['width'] = $this->width;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoPreviewResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['audio_format'])) {
            $model->audioFormat = $map['audio_format'];
        }
        if (isset($map['bitrate'])) {
            $model->bitrate = $map['bitrate'];
        }
        if (isset($map['duration'])) {
            $model->duration = $map['duration'];
        }
        if (isset($map['frame_rate'])) {
            $model->frameRate = $map['frame_rate'];
        }
        if (isset($map['height'])) {
            $model->height = $map['height'];
        }
        if (isset($map['sprite_info'])) {
            $model->spriteInfo = VideoPreviewSprite::fromMap($map['sprite_info']);
        }
        if (isset($map['template_list'])) {
            if (!empty($map['template_list'])) {
                $model->templateList = [];
                $n                   = 0;
                foreach ($map['template_list'] as $item) {
                    $model->templateList[$n++] = null !== $item ? VideoPreviewTranscode::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['thumbnail'])) {
            $model->thumbnail = $map['thumbnail'];
        }
        if (isset($map['video_format'])) {
            $model->videoFormat = $map['video_format'];
        }
        if (isset($map['width'])) {
            $model->width = $map['width'];
        }

        return $model;
    }
}
