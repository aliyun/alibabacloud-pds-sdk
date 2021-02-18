<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class VideoPreviewSprite extends Model
{
    /**
     * @description col
     *
     * @example 10
     *
     * @var int
     */
    public $col;

    /**
     * @description count
     *
     * @example 4
     *
     * @var int
     */
    public $count;

    /**
     * @description frame_count
     *
     * @example 333
     *
     * @var int
     */
    public $frameCount;

    /**
     * @description frame_height
     *
     * @example 90
     *
     * @var int
     */
    public $frameHeight;

    /**
     * @description frame_width
     *
     * @example 160
     *
     * @var int
     */
    public $frameWidth;

    /**
     * @description row
     *
     * @example 10
     *
     * @var int
     */
    public $row;

    /**
     * @description status
     *
     * @example finished
     *
     * @var string
     */
    public $status;
    protected $_name = [
        'col'         => 'col',
        'count'       => 'count',
        'frameCount'  => 'frame_count',
        'frameHeight' => 'frame_height',
        'frameWidth'  => 'frame_width',
        'row'         => 'row',
        'status'      => 'status',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->col) {
            $res['col'] = $this->col;
        }
        if (null !== $this->count) {
            $res['count'] = $this->count;
        }
        if (null !== $this->frameCount) {
            $res['frame_count'] = $this->frameCount;
        }
        if (null !== $this->frameHeight) {
            $res['frame_height'] = $this->frameHeight;
        }
        if (null !== $this->frameWidth) {
            $res['frame_width'] = $this->frameWidth;
        }
        if (null !== $this->row) {
            $res['row'] = $this->row;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return VideoPreviewSprite
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['col'])) {
            $model->col = $map['col'];
        }
        if (isset($map['count'])) {
            $model->count = $map['count'];
        }
        if (isset($map['frame_count'])) {
            $model->frameCount = $map['frame_count'];
        }
        if (isset($map['frame_height'])) {
            $model->frameHeight = $map['frame_height'];
        }
        if (isset($map['frame_width'])) {
            $model->frameWidth = $map['frame_width'];
        }
        if (isset($map['row'])) {
            $model->row = $map['row'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }

        return $model;
    }
}
