<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class VideoMediaAudioStream extends Model {
    protected $_name = [
        'bitRate' => 'bit_rate',
        'channelLayout' => 'channel_layout',
        'channels' => 'channels',
        'codeName' => 'code_name',
        'duration' => 'duration',
        'sampleRate' => 'sample_rate',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->bitRate) {
            $res['bit_rate'] = $this->bitRate;
        }
        if (null !== $this->channelLayout) {
            $res['channel_layout'] = $this->channelLayout;
        }
        if (null !== $this->channels) {
            $res['channels'] = $this->channels;
        }
        if (null !== $this->codeName) {
            $res['code_name'] = $this->codeName;
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
     * @return VideoMediaAudioStream
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['bit_rate'])){
            $model->bitRate = $map['bit_rate'];
        }
        if(isset($map['channel_layout'])){
            $model->channelLayout = $map['channel_layout'];
        }
        if(isset($map['channels'])){
            $model->channels = $map['channels'];
        }
        if(isset($map['code_name'])){
            $model->codeName = $map['code_name'];
        }
        if(isset($map['duration'])){
            $model->duration = $map['duration'];
        }
        if(isset($map['sample_rate'])){
            $model->sampleRate = $map['sample_rate'];
        }
        return $model;
    }
    /**
     * @description bit_rate 音频比特率 单位：bps
     * @example "129280"
     * @var string
     */
    public $bitRate;

    /**
     * @description channel_layout 声道布局
     * @example "5.1", "stereo"
     * @var string
     */
    public $channelLayout;

    /**
     * @description channels 音频数/声道数
     * @example 2
     * @var int
     */
    public $channels;

    /**
     * @description code_name 音频编码模式
     * @example "aac"
     * @var string
     */
    public $codeName;

    /**
     * @description duration 单位 秒
     * @example "7704.573000"
     * @var string
     */
    public $duration;

    /**
     * @description sample_rate 音频采样率
     * @example "48000"
     * @var string
     */
    public $sampleRate;

}
