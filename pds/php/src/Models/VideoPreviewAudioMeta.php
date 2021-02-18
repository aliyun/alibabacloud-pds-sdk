<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoPreviewAudioMeta extends Model
{
    /**
     * @description bitrate
     *
     * @example 349461
     *
     * @var float
     */
    public $bitrate;

    /**
     * @description channels
     *
     * @example 2
     *
     * @var int
     */
    public $channels;

    /**
     * @description duration
     *
     * @example 18.2
     *
     * @var float
     */
    public $duration;

    /**
     * @description sample_rate
     *
     * @example 18.2
     *
     * @var float
     */
    public $sampleRate;
    protected $_name = [
        'bitrate'    => 'bitrate',
        'channels'   => 'channels',
        'duration'   => 'duration',
        'sampleRate' => 'sample_rate',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->bitrate) {
            $res['bitrate'] = $this->bitrate;
        }
        if (null !== $this->channels) {
            $res['channels'] = $this->channels;
        }
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }
        if (null !== $this->sampleRate) {
            $res['sample_rate'] = $this->sampleRate;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoPreviewAudioMeta
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['bitrate'])) {
            $model->bitrate = $map['bitrate'];
        }
        if (isset($map['channels'])) {
            $model->channels = $map['channels'];
        }
        if (isset($map['duration'])) {
            $model->duration = $map['duration'];
        }
        if (isset($map['sample_rate'])) {
            $model->sampleRate = $map['sample_rate'];
        }

        return $model;
    }
}
