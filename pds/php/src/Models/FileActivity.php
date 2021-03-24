<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class FileActivity extends Model
{
    /**
     * @description Actors
     *
     * @example ""
     *
     * @var Actor[]
     */
    public $actors;

    /**
     * @var ActionDetail
     */
    public $primaryActionDetail;

    /**
     * @description Targets
     *
     * @example ""
     *
     * @var Target[]
     */
    public $targets;

    /**
     * @var TimeRange
     */
    public $timeRange;

    /**
     * @description Timestamp
     *
     * @example ""
     *
     * @var string
     */
    public $timestamp;
    protected $_name = [
        'actors'              => 'actors',
        'primaryActionDetail' => 'primary_action_detail',
        'targets'             => 'targets',
        'timeRange'           => 'time_range',
        'timestamp'           => 'timestamp',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->actors) {
            $res['actors'] = [];
            if (null !== $this->actors && \is_array($this->actors)) {
                $n = 0;
                foreach ($this->actors as $item) {
                    $res['actors'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->primaryActionDetail) {
            $res['primary_action_detail'] = null !== $this->primaryActionDetail ? $this->primaryActionDetail->toMap() : null;
        }
        if (null !== $this->targets) {
            $res['targets'] = [];
            if (null !== $this->targets && \is_array($this->targets)) {
                $n = 0;
                foreach ($this->targets as $item) {
                    $res['targets'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->timeRange) {
            $res['time_range'] = null !== $this->timeRange ? $this->timeRange->toMap() : null;
        }
        if (null !== $this->timestamp) {
            $res['timestamp'] = $this->timestamp;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return FileActivity
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['actors'])) {
            if (!empty($map['actors'])) {
                $model->actors = [];
                $n             = 0;
                foreach ($map['actors'] as $item) {
                    $model->actors[$n++] = null !== $item ? Actor::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['primary_action_detail'])) {
            $model->primaryActionDetail = ActionDetail::fromMap($map['primary_action_detail']);
        }
        if (isset($map['targets'])) {
            if (!empty($map['targets'])) {
                $model->targets = [];
                $n              = 0;
                foreach ($map['targets'] as $item) {
                    $model->targets[$n++] = null !== $item ? Target::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['time_range'])) {
            $model->timeRange = TimeRange::fromMap($map['time_range']);
        }
        if (isset($map['timestamp'])) {
            $model->timestamp = $map['timestamp'];
        }

        return $model;
    }
}
