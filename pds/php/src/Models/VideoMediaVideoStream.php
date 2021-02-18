<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoMediaVideoStream extends Model
{
    /**
     * @description bitrate 视频比特率 单位：bps
     *
     * @example "108420"
     *
     * @var string
     */
    public $bitrate;

    /**
     * @description clarity 清晰度（扫描）
     *
     * @example "1080P"
     *
     * @var string
     */
    public $clarity;

    /**
     * @description code_name 视频编码模式
     *
     * @example "h264"
     *
     * @var string
     */
    public $codeName;

    /**
     * @description duration 单位 秒
     *
     * @example "7704.573000"
     *
     * @var string
     */
    public $duration;

    /**
     * @description fps 视频平均帧率
     *
     * @example "25/1"
     *
     * @var string
     */
    public $fps;

    /**
     * @description rotate 视频横屏 竖屏
     *
     * @var string
     */
    public $rotate;
    protected $_name = [
        'bitrate'  => 'bitrate',
        'clarity'  => 'clarity',
        'codeName' => 'code_name',
        'duration' => 'duration',
        'fps'      => 'fps',
        'rotate'   => 'rotate',
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
        if (null !== $this->clarity) {
            $res['clarity'] = $this->clarity;
        }
        if (null !== $this->codeName) {
            $res['code_name'] = $this->codeName;
        }
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }
        if (null !== $this->fps) {
            $res['fps'] = $this->fps;
        }
        if (null !== $this->rotate) {
            $res['rotate'] = $this->rotate;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoMediaVideoStream
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['bitrate'])) {
            $model->bitrate = $map['bitrate'];
        }
        if (isset($map['clarity'])) {
            $model->clarity = $map['clarity'];
        }
        if (isset($map['code_name'])) {
            $model->codeName = $map['code_name'];
        }
        if (isset($map['duration'])) {
            $model->duration = $map['duration'];
        }
        if (isset($map['fps'])) {
            $model->fps = $map['fps'];
        }
        if (isset($map['rotate'])) {
            $model->rotate = $map['rotate'];
        }

        return $model;
    }
}
