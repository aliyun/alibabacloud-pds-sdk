<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoMediaResponse extends Model
{
    /**
     * @description address_line
     *
     * @example 北京市昌平区白各庄新村路
     *
     * @var string
     */
    public $addressLine;

    /**
     * @description city
     *
     * @example 杭州
     *
     * @var string
     */
    public $city;

    /**
     * @description country
     *
     * @example 中国
     *
     * @var string
     */
    public $country;

    /**
     * @description district
     *
     * @example 余杭区
     *
     * @var string
     */
    public $district;

    /**
     * @description duration 单位 秒
     *
     * @example "7704.573000"
     *
     * @var string
     */
    public $duration;

    /**
     * @description height
     *
     * @example 720
     *
     * @var int
     */
    public $height;

    /**
     * @description location
     *
     * @example 40.110333,116.349311
     *
     * @var string
     */
    public $location;

    /**
     * @description province
     *
     * @example 浙江省
     *
     * @var string
     */
    public $province;

    /**
     * @description time
     *
     * @var string
     */
    public $time;

    /**
     * @description township
     *
     * @example 沙河镇
     *
     * @var string
     */
    public $township;

    /**
     * @var VideoMediaAudioStream[]
     */
    public $videoMediaAudioStream;

    /**
     * @var VideoMediaVideoStream[]
     */
    public $videoMediaVideoStream;

    /**
     * @description width
     *
     * @example 1024
     *
     * @var int
     */
    public $width;
    protected $_name = [
        'addressLine'           => 'address_line',
        'city'                  => 'city',
        'country'               => 'country',
        'district'              => 'district',
        'duration'              => 'duration',
        'height'                => 'height',
        'location'              => 'location',
        'province'              => 'province',
        'time'                  => 'time',
        'township'              => 'township',
        'videoMediaAudioStream' => 'video_media_audio_stream',
        'videoMediaVideoStream' => 'video_media_video_stream',
        'width'                 => 'width',
    ];
    protected $_default = [
        'height' => 0,
        'width'  => 0,
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->addressLine) {
            $res['address_line'] = $this->addressLine;
        }
        if (null !== $this->city) {
            $res['city'] = $this->city;
        }
        if (null !== $this->country) {
            $res['country'] = $this->country;
        }
        if (null !== $this->district) {
            $res['district'] = $this->district;
        }
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }
        if (null !== $this->height) {
            $res['height'] = $this->height;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->province) {
            $res['province'] = $this->province;
        }
        if (null !== $this->time) {
            $res['time'] = $this->time;
        }
        if (null !== $this->township) {
            $res['township'] = $this->township;
        }
        if (null !== $this->videoMediaAudioStream) {
            $res['video_media_audio_stream'] = [];
            if (null !== $this->videoMediaAudioStream && \is_array($this->videoMediaAudioStream)) {
                $n = 0;
                foreach ($this->videoMediaAudioStream as $item) {
                    $res['video_media_audio_stream'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->videoMediaVideoStream) {
            $res['video_media_video_stream'] = [];
            if (null !== $this->videoMediaVideoStream && \is_array($this->videoMediaVideoStream)) {
                $n = 0;
                foreach ($this->videoMediaVideoStream as $item) {
                    $res['video_media_video_stream'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->width) {
            $res['width'] = $this->width;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoMediaResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['address_line'])) {
            $model->addressLine = $map['address_line'];
        }
        if (isset($map['city'])) {
            $model->city = $map['city'];
        }
        if (isset($map['country'])) {
            $model->country = $map['country'];
        }
        if (isset($map['district'])) {
            $model->district = $map['district'];
        }
        if (isset($map['duration'])) {
            $model->duration = $map['duration'];
        }
        if (isset($map['height'])) {
            $model->height = $map['height'];
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }
        if (isset($map['province'])) {
            $model->province = $map['province'];
        }
        if (isset($map['time'])) {
            $model->time = $map['time'];
        }
        if (isset($map['township'])) {
            $model->township = $map['township'];
        }
        if (isset($map['video_media_audio_stream'])) {
            if (!empty($map['video_media_audio_stream'])) {
                $model->videoMediaAudioStream = [];
                $n                            = 0;
                foreach ($map['video_media_audio_stream'] as $item) {
                    $model->videoMediaAudioStream[$n++] = null !== $item ? VideoMediaAudioStream::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['video_media_video_stream'])) {
            if (!empty($map['video_media_video_stream'])) {
                $model->videoMediaVideoStream = [];
                $n                            = 0;
                foreach ($map['video_media_video_stream'] as $item) {
                    $model->videoMediaVideoStream[$n++] = null !== $item ? VideoMediaVideoStream::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['width'])) {
            $model->width = $map['width'];
        }

        return $model;
    }
}
